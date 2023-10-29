# Import necessary modules
import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from sklearn.metrics import mean_absolute_percentage_error

# Default settings
DEFAULT_DATE = "2015-01-01"
CURRENT_DATE = date.today().strftime("%Y-%m-%d")

st.title('Enhanced Stock Forecasting Tool')

def fetch_stock_data(stock_symbol, start_date):
    """
    Retrieve historical stock data for a given ticker and date range.
    """
    try:
        stock_data = yf.download(stock_symbol, start_date, CURRENT_DATE)
        stock_data.reset_index(inplace=True)
        return stock_data
    except Exception as e:
        st.error(f"Error encountered: {e}")
        return None

def visualize_stock_data(stock_data):
    """
    Display the stock's opening and closing prices over a timeline.
    """
    visualization = go.Figure()
    visualization.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Open'], name="Opening Price"))
    visualization.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name="Closing Price"))
    visualization.layout.update(title_text='Time Series Visualization with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(visualization)

def compute_mape(actual_data, predicted_data):
    """
    Compute Mean Absolute Percentage Error (MAPE).
    """
    forecast_subset = predicted_data.loc[:len(actual_data)-1]
    mape_value = mean_absolute_percentage_error(actual_data['y'], forecast_subset['yhat'])
    return mape_value

# User Interface Elements
stock_symbol_input = st.text_input('Input stock ticker for forecasting (e.g. AAPL, GOOG):').upper()
chosen_start_date = st.date_input('Choose start date for historical data:', DEFAULT_DATE)
forecast_years = st.slider('Forecast duration (in years):', 1, 4)
forecast_duration = forecast_years * 365

stock_data_status = st.text('Fetching stock data...')
stock_data = fetch_stock_data(stock_symbol_input, chosen_start_date)

if stock_data is not None:
    stock_data_status.text('Stock data fetched successfully!')

    st.subheader('Historical Stock Data')
    st.write(stock_data.tail())

    visualize_stock_data(stock_data)

    training_data = stock_data[['Date','Close']]
    training_data = training_data.rename(columns={"Date": "ds", "Close": "y"})

    # User-adjustable Prophet parameters
    seasonality_choice = st.selectbox('Choose Seasonality Mode:', ['additive', 'multiplicative'])
    yearly_pattern = st.slider('Set Yearly Seasonality:', 1, 20, 10)

    model = Prophet(seasonality_mode=seasonality_choice, yearly_seasonality=yearly_pattern)
    model.fit(training_data)
    future_dates = model.make_future_dataframe(periods=forecast_duration)
    predictions = model.predict(future_dates)

    st.subheader('Forecasted Data')
    st.write(predictions.tail())

    st.write(f'Forecast visualization for {forecast_years} years')
    forecast_plot = plot_plotly(model, predictions)
    st.plotly_chart(forecast_plot)

    st.write("Forecast Breakdown")
    components_plot = model.plot_components(predictions)
    st.write(components_plot)

    st.subheader('Model Accuracy')
    mape_result = compute_mape(training_data, predictions)
    st.write(f'Mean Absolute Percentage Error (MAPE): {mape_result:.2f}%')
else:
    st.warning("Please input a valid stock ticker and try again.")
