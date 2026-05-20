import joblib

def test_pipeline_loads():
    pipe = joblib.load("./BestModel/pipeline_complet.joblib")
    assert pipe is not None

def test_pipeline_accepts_example():
    df_example = joblib.load("./data/app_test_clean_v2.joblib")
    pipe = joblib.load("./BestModel/pipeline_complet.joblib")

    sample = df_example.sample(1)
    score = pipe.predict_proba(sample)[0][1]

    assert 0 <= score <= 1
