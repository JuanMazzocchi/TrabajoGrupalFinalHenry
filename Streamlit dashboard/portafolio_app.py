import streamlit as st
import pandas as pd
# import pandas_datareader.data as web
import datetime
from PIL import Image
import matplotlib.pyplot as plt
# import matplotlib as mpl
import mplcyberpunk
# import numpy as np
from prophet import Prophet
import json
# import matplotlib.dates as mdates
import plotly.express as px

plt.style.use("seaborn-v0_8-bright")
# print(plt.style.available)
###########################
#### Funciones Principales
###########################

st.markdown(
    """
    <style>
        .st-emotion-cache-18ni7ap{
            background-color:rgba(0,0,0,0);
                 
        }
        .main {
                background-color: #0b00ff;
                background-image: 
                radial-gradient(at 47% 33%, hsl(260.90, 86%, 35%) 0, transparent 80%), 
                radial-gradient(at 10% 10%, hsl(131.90, 100%, 50%) 0, transparent 55%);


        }
        .st-emotion-cache-16txtl3{
            background-color:'light-gray';
        }
           /* Cambia el color del título (h1) */
         h1 {
            color:white; /* Puedes cambiar el color a tu preferencia */
        }

        /* Cambia el color del subtitulo (h2) */
         h2 {
            color:white; /* Puedes cambiar el color a tu preferencia */
        }
         h3 {
            color:white; /* Puedes cambiar el color a tu preferencia */
        }
         body {
            width: 90%;  /* Puedes ajustar este valor según tus preferencias */
            margin: auto;
        }
        .block-container{
            width: 90% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def get_data(stock):
    
    if stock=="Belleza y Salud":
        df = pd.read_csv('data/Belleza y SaludDSY.csv',sep=';')
        return df
    elif stock == 'Auto':
        df = pd.read_csv('data/AutoDSY.csv',sep=';')
        return df
    elif stock == 'Ocio y Deportes':
        df = pd.read_csv('data/Ocio y DeportesDSY.csv',sep=';')
        return df
    elif stock == "Accesorios de Computadoras":
        df = pd.read_csv('data/Accesorios de ComputadorasDSY.csv',sep=';')
        return df
    elif stock == "Decoración de muebles":
        df = pd.read_csv('data/Decoración de mueblesDSY.csv',sep=';')
        return df
    elif stock == "Mesa, Baño , Cama":
        df = pd.read_csv('data/Mesa, Baño , CamaDSY.csv',sep=';')
        return df
    elif stock == "Cosas Interesantes":
        df = pd.read_csv('data/Cosas InteresantesDSY.csv',sep=';')
        return df
    elif stock == "Artículos para el hogar":
        df = pd.read_csv('data/Artículos para el hogarDSY.csv',sep=';')
        return df
    elif stock == "Relojes y Regalos":
        df = pd.read_csv('data/Relojes y RegalosDSY.csv',sep=';')
        return df
    elif stock == "Juguetes":
        df = pd.read_csv('data/JuguetesDSY.csv',sep=';')
        return df
        
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode

     
    
def plot_prophet(data, n_forecast=1460):
    # data_prophet = data.reset_index().copy()
    # data_prophet.rename(columns={'Date':'ds','Close':'y'}, inplace=True)
    if pandemia == True:
        m = Prophet(yearly_seasonality= True, uncertainty_samples = 500, mcmc_samples=50, interval_width= 0.6)
        m.fit(data[['ds','y']])

        future = m.make_future_dataframe(periods=n_forecast)
        
        forecast = m.predict(future)
        
        forecast.loc[forecast.ds > '2020-01-01'  , 'yhat']*=1.4
        
        forecast.loc[forecast.ds > '2020-01-01'  , 'yhat_lower']*=1.4
        
        forecast.loc[forecast.ds > '2020-01-01' , 'yhat_upper']*=1.4
        
    

        fig1=m.plot(forecast)
        # background=plt.imread('assets/g7logo3.jpg')
        # background = plt.imread('assets/logo_source.png')
        mplcyberpunk.add_glow_effects()
        ax = plt.gca()
        # ax.patch.set_facecolor('white')
        # ax.figure.figimage(background, 60, 60, alpha=.15, zorder=1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.grid(True,color='gray', linestyle='-', linewidth=0.4)
        plt.xticks(rotation=45,  ha='right')
        plt.ylabel('Ventas')
        plt.xlabel('Fecha')
        fig1=plt.gcf()
        fig1.set_facecolor('white')
         
        plt.plot(forecast.ds, forecast.yhat, color='green', linewidth=0.5)
         
        return fig1
        
        
         
    m = Prophet(yearly_seasonality= True, uncertainty_samples = 500, mcmc_samples=50, interval_width= 0.6)
    m.fit(data[['ds','y']])

    future = m.make_future_dataframe(periods=n_forecast)
    forecast = m.predict(future)
    fig1 = m.plot(forecast)
    # background = plt.imread('assets/logo_source.png')
    # mplcyberpunk.add_glow_effects()
    ax = plt.gca()
    # ax.figure.figimage(background, 40, 40, alpha=.15, zorder=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.grid(True,color='gray', linestyle='-', linewidth=0.4)
    plt.xticks(rotation=45,  ha='right')
    plt.ylabel('Ventas')
    plt.xlabel('Fecha')
    
    plt.plot(forecast.ds, forecast.yhat, color='green', linewidth=0.5)
    return fig1

    
    
        
def render_basic_line():
    
        options = {
            "tooltip": {"trigger": "axis"},
            "xAxis": {
                "type": "category",
                "data":data['ds'].tolist(),
                "axisLabel": {"color": "white"}
            },
            "yAxis": {"type": "value"}, "axisLabel": {"color": "white"},
            "series": [
                {"data": data['y'].tolist(), "type": "line"}
            ],
            "backgroundColor": 'rgba(0,0,0,0)',
            "color":'green',
            
            }
            
        
        st_echarts(
            options=options, height="400px",
        )
        # st_echarts(
        #     options=options, height="400px", theme="dark",
        # )
        
        
def render_stacked_line_chart():
    
    rango_fechas = pd.date_range(start='2016-10', end='2018-08', freq='MS')
    lista_meses = [fecha.strftime('%Y-%m') for fecha in rango_fechas]
    
    
    belleza=pd.read_csv('data/Belleza y SaludDSY.csv',sep=';')
    belleza['ds']=pd.to_datetime(belleza['ds'])
    belleza.set_index('ds',inplace=True)
    belleza=belleza.resample('M').sum()
    fecha_a_eliminar = pd.to_datetime('2016-09-30')
    belleza = belleza[belleza.index != fecha_a_eliminar]
    
    relojes=pd.read_csv('data/Relojes y RegalosDSY.csv',sep=';')
    relojes['ds']=pd.to_datetime(relojes['ds'])
    relojes.set_index('ds',inplace=True)
    relojes=relojes.resample('M').sum()
    
    mesa=pd.read_csv('data/Mesa, Baño , CamaDSY.csv',sep=';')
    mesa['ds']=pd.to_datetime(mesa['ds'])
    mesa.set_index('ds',inplace=True)
    mesa=mesa.resample('M').sum()
    
    ocio=pd.read_csv('data/Ocio y DeportesDSY.csv',sep=';')
    ocio['ds']=pd.to_datetime(ocio['ds'])
    ocio.set_index('ds',inplace=True)
    ocio=ocio.resample('M').sum()
    
    compu=pd.read_csv('data/Accesorios de ComputadorasDSY.csv',sep=';')
    compu['ds']=pd.to_datetime(compu['ds'])
    compu.set_index('ds',inplace=True)
    compu=compu.resample('M').sum()
    
    
    options = {
        # "title": {"text":"Categorias \n","color":'white'},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["Belleza y Salud", "Relojes y Regalos", "Mesa, Baño y Cama", "Ocio y Deporte", "Acc. de Computacion"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": lista_meses,
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "Belleza y Salud",
                "type": "line",
                # "stack": "总量",
                "data": belleza['y'].tolist(),
            },
            {
                "name": "Relojes y Regalos",
                "type": "line",
                # "stack": "总量",
                "data":  relojes['y'].tolist(),
            },
            {
                "name": "Mesa, Baño y Cama",
                "type": "line",
                # "stack": "总量",
                "data": mesa['y'].tolist(),
            },
            {
                "name": "Ocio y Deporte",
                "type": "line",
                # "stack": "总量",
                "data": ocio['y'].tolist(),
            },
            {
                "name": "Acc. de Computacion",
                "type": "line",
                # "stack": "总量",
                "data": compu['y'].tolist(),
            },
        ],
    }
    # mplcyberpunk.add_glow_effects()
    st_echarts(options=options, height="400px",theme='dark')
    
def catXestado( stock, estado,periods=1460 ):

    df=pd.read_csv('data/Tabla1FinalCorrejida.csv', sep=';')
    df['order_purchase_timestamp']=pd.to_datetime(df['order_purchase_timestamp'])
    df['fecha']= df['order_purchase_timestamp'].dt.date
    print(stock+'   '+ estado)
    # print(df.head())
    
    dfCat=df[df['product_category_name']== stock]
    dfCatEst=dfCat[dfCat['Estados']==estado]
    
    dfCatEst['fecha']=pd.to_datetime(dfCatEst['fecha'])
    dfCatEst=dfCatEst.groupby('fecha')['price'].sum().reset_index()
    dfCatEst.reset_index(level=0,inplace=True)
    dfCatEst.rename(columns={'fecha':'ds','price':'y'}, inplace=True)
    
    m = Prophet(yearly_seasonality= True, uncertainty_samples = 50, mcmc_samples=50, interval_width= 0.6)
    m.fit(dfCatEst[['ds','y']])

    future = m.make_future_dataframe(periods=periods)
    forecast = m.predict(future)
    fig2 = m.plot(forecast)
    # background = plt.imread('assets/logo_source.png')
    # mplcyberpunk.add_glow_effects()
    ax = plt.gca()
    # ax.figure.figimage(background, 40, 40, alpha=.15, zorder=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.grid(True,color='white', linestyle='-', linewidth=0.6)
    plt.xticks(rotation=45,  ha='right')
    plt.ylabel('Ventas')
    plt.xlabel('Fecha')
    
    plt.plot(forecast.ds, forecast.yhat, color='green', linewidth=0.5)
    return fig2
    
    
###########################
#### LAYOUT - Sidebar
###########################

logo_pypro = Image.open('assets/g7logo3.jpg')

with st.sidebar:
    st.image(logo_pypro)
    stock = st.selectbox('Categorías', ['Belleza y Salud', 'Auto', 'Ocio y Deportes','Accesorios de Computadoras', 'Decoración de muebles','Mesa, Baño , Cama', 'Cosas Interesantes','Artículos para el hogar', 'Relojes y Regalos', 'Juguetes'], index=1)
    estados=st.selectbox('Estados', ['Acre', ' Alagoas', ' Amazonas', 'Bahia', ' Ceara',' Distrito Federal', ' Espirito Santo', ' Goias', ' Maranhao',' Mato Grosso', ' Mato Grosso do Sul', ' Minas Gerais', ' Para',' Paraiba', 'Parana', ' Pernambuco', 'Pernambuco', ' Piaui','Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',' Rondonia', ' Roraima', ' Santa Catarina', 'Sao Paulo',' Sergipe', ' Tocantins'], index=1)
    
    pandemia=st.checkbox('Añadir efecto pandemia', value=False)
    
    periods = st.slider('Días de Forecast', value=1460, min_value=602, max_value=3000)


###########################
#### DATA - Funciones sobre inputs
###########################

data = get_data(stock)


plot_forecast = plot_prophet(data, periods)



###########################
#### LAYOUT - Render Final
###########################

st.title(f"Predicción de Ventas : {stock}")

st.subheader('Ventas por día históricas')
render_basic_line()

st.subheader('Forecast - Prophet de ventas por día')
st.pyplot(plot_forecast)

st.subheader('Forecast - Plotly, sin Máximos ni mínimos')
 
 
 
st.plotly_chart(plot_forecast, use_container_width=True, theme='streamlit')

st.subheader('Top 5 Categorías más vendidas históricas')
render_stacked_line_chart()


st.subheader(f'Predicción de Categoría: {stock} (Ventas por día)')
st.subheader(f'Estado : {estados}')
st.pyplot(catXestado(stock,estados,periods))
st.subheader('Sin Máximos ni mínimos')
st.plotly_chart(catXestado(stock,estados,periods), use_container_width=True )
 
