import plotly.express as px
import pandas as pd
import time
import datetime
import streamlit as st  # 🎈 data web app development
import serial
import serial.tools.list_ports

SERIAL_DATA_LIST = []
test = ''

st.set_page_config(
    page_title="My Datalogger",
    page_icon="✅",
    layout="wide",
)

ports = serial.tools.list_ports.comports()
port_list = [p.device for p in ports]

print(port_list)

# port_list = ["COM1", "COM2", "COM3", "COM4", "COM5"]


# port_selection = st.sidebar.selectbox("Select Port", [0] + port_list)
port_selection = st.sidebar.text_input("Enter port: ", value=0)
print(port_selection)

baud_rate = st.sidebar.text_input("Enter baud rate: ", value=9600)
print(baud_rate)

count1 = 0
count2 = 0
ct = datetime.datetime.now()

data_dict = {'time': [str(ct)], 'serial': [count2]}
df = pd.DataFrame.from_dict(data_dict)

st.title("Datalogger")

# creating a single-element container
placeholder = st.empty()

com_error_text = ''

try:
    ardSerialData = serial.Serial(port_selection, baud_rate)
    com_error_text = st.write('')
    st.write("Arduino Connected")
    while True:
        if ardSerialData.inWaiting() > 0:
            myData = ardSerialData.readline().decode()
            # st.text(myData)
            ct = datetime.datetime.now()

            df.loc[len(df.index)] = [str(ct), myData]

            # df["var1_new"] = count1
            # df["var2_new"] = count2

            with placeholder.container():
                fig_col1, fig_col2 = st.columns(2)

                with fig_col1:
                    # st.markdown("### Live Chart")
                    fig = px.line(df, x="time", y="serial", title=f'Arduino Serial Data - {myData}')
                    # fig.show()
                    st.write(fig)

                with fig_col2:
                    # st.markdown("### Live Chart")
                    fig2 = px.line(df, x="time", y="serial", title=f'Arduino Serial Data - {myData}')
                    # fig.show()
                    st.write(fig2)

                # with fig_col2:
                #     st.markdown("### Second Chart")
                #     fig2 = px.histogram(data_frame=df, x="var1_new")
                #     st.write(fig2)

                st.markdown("### Detailed Data View")
                st.dataframe(df)
                # print(df)
                # time.sleep(2)
            # print('Serial Da ta: ',  myData)
            # myList.append(myData)
except:
    st.error('Please select the right port and try again.', icon="🚨")

    # com_error_text = st.write("Testttt")

# while True:
#     count1 += 1
#     count2 += 2
#
#     ct = datetime.datetime.now()
#     df.loc[len(df.index)] = [str(ct), count2]
#
#     # df["var1_new"] = count1
#     # df["var2_new"] = count2
#
#     with placeholder.container():
#         fig_col1, fig_col2 = st.columns(2)
#
#         with fig_col1:
#             st.markdown("### Live Chart")
#             fig = px.line(df, x="var1", y="var2", title='Test data live graph')
#             # fig.show()
#             st.write(fig)
#
#         # with fig_col2:
#         #     st.markdown("### Second Chart")
#         #     fig2 = px.histogram(data_frame=df, x="var1_new")
#         #     st.write(fig2)
#
#         st.markdown("### Detailed Data View")
#         st.dataframe(df)
#         # print(df)
#         time.sleep(2)

# df = px.data.gapminder().query("continent=='Oceania'")
# print(df)
