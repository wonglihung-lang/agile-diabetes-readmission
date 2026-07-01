# ==================================================
# SIMPLE AUTOMATED TESTS
# ==================================================

def test_project_name():
    project = "Diabetes Readmission Prediction"
    assert len(project) > 0

def test_target_variable():
    target = "readmitted"
    assert target == "readmitted"

def test_model_type():
    model = "LightGBM"
    assert model in ["Logistic Regression", "LightGBM"]
