import kfp
from kfp import dsl

from kfp_preprocess_component import preprocess_op
from kfp import compiler



@dsl.pipeline(
    name = 'Calfornia Housing Pipeline',
    description= 'Calfornia Housing Pipeline'
)
def cal_pipeline():
    p = preprocess_op()

compiler.Compiler().compile(cal_pipeline, package_path='pipeline.yaml')

client = kfp.Client(host = 'http://127.0.0.1:60029')
client.create_run_from_pipeline_package('pipeline.yaml', arguments={'param': 'a', 'other_param': 2})
client.create_run_from_pipeline_func('pipeline.yaml', arguments={'param': 'a', 'other_param': 2})

client.create_run_from_pipeline_func(cal_pipeline,arguments={},experiment_name="my-experiment", run_name="test-run-1", namespace="kubeflow-user-example-com")