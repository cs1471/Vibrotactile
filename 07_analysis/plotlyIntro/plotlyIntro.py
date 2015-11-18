import plotly as py
import plotly.tools as tls

version = py.__version__ # make sure most up to date version

py.sign_in('cs1471', '9xknhmjhas') #sign in to plotly server with your UN and api key

tls.set_credentials_file(username="cs1471",
                             api_key="9xknhmjhas")

credentials = tls.get_credentials_file()