import joblib

df_example = joblib.load("./data/app_test_small.joblib")
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

def test_pipeline_loads():
    assert pipe is not None

def test_pipeline_accepts_example():
    sample = df_example.sample(1)
    score = pipe.predict_proba(sample)[0][1]

    assert 0 <= score <= 1
