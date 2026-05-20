import joblib

df = joblib.load("data/app_test_clean_v2.joblib")
df_small = df.sample(50)
joblib.dump(df_small, "data/app_test_small.joblib")
