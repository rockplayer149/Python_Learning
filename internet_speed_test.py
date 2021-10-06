from speedtest import Speedtest

st = Speedtest()

print("Your Downloading speed is : ", st.download())
print("Your Uploading speed is : ", st.upload())