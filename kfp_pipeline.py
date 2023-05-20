import kfp
from kfp import dsl

from kfp_preprocess_component import preprocess_op


@dsl.pipeline(
    name = 'Calfornia Housing Pipeline',
    description= 'Calfornia Housing Pipeline'
)
def cal_pipeline():
    p = preprocess_op()

client = kfp.Client()
client.create_run_from_pipeline_func(cal_pipeline,arguments={},experiment_name="my-experiment", run_name="test-run-1", namespace="kubeflow-user-example-com")