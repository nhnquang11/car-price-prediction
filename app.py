import streamlit as st
import pickle
import pandas as pd
import json
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('./data.csv')
X = df.drop('Giá thành', axis=1)
y = df['Giá thành']
X.drop(["Đơn vị động cơ", "Số chỗ ngồi", "Số cửa"], axis=1, inplace=True)
X = pd.get_dummies(X,
                   columns=["Thương hiệu", "Tình trạng", "Xuất xứ", "Kiểu dáng", "Hộp số", "Dẫn động",
                            "Loại nhiên liệu", "Model"],
                   drop_first=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
dt = DecisionTreeRegressor(
    max_depth=None, min_samples_leaf=2, min_samples_split=10, random_state=42)
dt.fit(X_scaled, y)

with open('./data.json', 'r') as json_file:
    data = json.load(json_file)

with open('./models/DecisionTree.pkl', 'rb') as file:
    dt = pickle.load(file)

brand = st.selectbox('Car brand:', sorted(data.keys()))
model = st.selectbox('Model:', sorted(data[brand].keys()))
seats = data[brand][model]['Số chỗ ngồi']
doors = data[brand][model]['Số cửa']
st.write("Number of seats:", seats, "Number of doors:", doors)
status = st.selectbox('Status:', ['New', 'Used'])
origin = st.selectbox('Origin:', sorted(data[brand][model]['Xuất xứ']))
style = st.selectbox('Style:', sorted(data[brand][model]['Kiểu dáng']))
gear = st.selectbox('Gear:', sorted(data[brand][model]['Hộp số']))
transmission = st.selectbox(
    'Transmission:', sorted(data[brand][model]['Dẫn động']))
fuel = st.selectbox(
    'Fuel type:', sorted(data[brand][model]['Loại nhiên liệu']))
cylinder = st.selectbox(
    'Cylinder capacity:', sorted(data[brand][model]['Dung tích động cơ']))
if status == 'New':
    km = 0
    st.write('Traveled Km:', km)
else:
    km = st.slider('Traveled Km:', 0, 150000, 0)
age = st.slider('Age:', 0, 50, 0)

submit_button = st.button('Predict')
if submit_button:
    user_input = {
        "Thương hiệu": brand,
        "Model": model,
        "Tình trạng": status,
        "Số Km đã đi": km,
        "Xuất xứ": origin,
        "Kiểu dáng": style,
        "Hộp số": gear,
        "Số chỗ ngồi": seats,
        "Số cửa": doors,
        "Dẫn động": transmission,
        "Loại nhiên liệu": fuel,
        "Dung tích động cơ": cylinder,
        "Tuổi": age
    }

    user_df = pd.DataFrame([user_input])
    columns_to_drop = ["Đơn vị động cơ", "Số chỗ ngồi", "Số cửa"]
    columns_to_drop_existing = [
        col for col in columns_to_drop if col in user_df.columns]
    user_df.drop(columns_to_drop_existing, axis=1, inplace=True)
    user_df = pd.get_dummies(user_df,
                             columns=["Thương hiệu", "Tình trạng", "Xuất xứ", "Kiểu dáng", "Hộp số", "Dẫn động",
                                      "Loại nhiên liệu", "Model"],
                             drop_first=True)
    missing_cols = list(set(X.columns) - set(user_df.columns))
    user_df = pd.concat([user_df, pd.DataFrame(
        0, index=user_df.index, columns=missing_cols)], axis=1)
    user_df = user_df[X.columns]
    user_df_scaled = scaler.transform(user_df)
    predicted_price = dt.predict(user_df_scaled)
    st.write("Predicted price:", predicted_price[0])
