import pandas as pd
import streamlit as st

# 1. Create an embedded sample dataset
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Sales': [120, 150, 170, 130, 200, 250, 220],
    'Visitors': [400, 450, 500, 420, 600, 750, 700],
}
df = pd.DataFrame(data)

# 2. App Title and Description
st.title('📊 Simple Weekly Dashboard')
st.write(
    'This app uses a built-in dataset to demonstrate basic Streamlit features.'
)

# 3. Display the Raw Dataset
st.subheader('Raw Data Table')
st.dataframe(df)

# 4. Add an Interactive Filter
st.subheader('Filter by Minimum Sales')
min_sales = st.slider(
    'Select minimum sales threshold:',
    int(df['Sales'].min()),
    int(df['Sales'].max()),
    120,
)
filtered_df = df[df['Sales'] >= min_sales]

st.write(f'Showing {len(filtered_df)} days matching your filter:')
st.dataframe(filtered_df)

# 5. Display a Chart
st.subheader('Weekly Sales Chart')
st.bar_chart(df.set_index('Day')['Sales'])
