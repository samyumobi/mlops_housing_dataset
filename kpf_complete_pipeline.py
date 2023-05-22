import kfp
from kfp import dsl
import kfp.dsl as dsl

from kfp_preprocess_component import preprocess_op
from kfp import compiler


def train_op(x_train,y_train):
    return dsl.ContainerOp(
        name='Train model',
        image='samyumobi99/train_pipeline:latest',
        arguments=['--x_train', x_train,
                   '--y_train',y_train],
        file_outputs={
            'model':'/app/model.pkl'
        }
    )

def test_op(x_test,y_test,model):
    return dsl.ContainerOp(
        name='Test model',
        image='samyumobi99/housing_test_pipeline:latest',
        arguments=['--x_test', x_test,
                   '--y_test',y_test,
                   '--model',model],
        file_outputs={
            'mean_squared_error':'/app/output.txt'
        }
    )


def deploy_model_op(model):
    return dsl.ContainerOp(
        name='Deploy model',
        image='samyumobi99/housing_deploy_pipeline:latest',
        arguments=['--model', model]
    )



@dsl.pipeline(
    name = 'Calfornia Housing Pipeline',
    description= 'Calfornia Housing Pipeline'
)
def cal_pipeline():
    _preprocess_op = preprocess_op()
    _train_op = train_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_train']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_train'])
    ).after(_preprocess_op)
    _test_op = test_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_test']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_test']),
        dsl.InputArgumentPath(_train_op.outputs['model'])
    ).after(_train_op)
    deploy_model_op(dsl.InputArgumentPath(_train_op.outputs['model'])).after(_test_op)

client = kfp.Client()
client.create_run_from_pipeline_func(cal_pipeline, arguments={})


# compiler.Compiler().compile(cal_pipeline, package_path='pipeline.yaml')

# client = kfp.Client(host = 'http://127.0.0.1:60029')
# client.create_run_from_pipeline_package('pipeline.yaml', arguments={'param': 'a', 'other_param': 2})
# client.create_run_from_pipeline_func('pipeline.yaml', arguments={'param': 'a', 'other_param': 2})
#
# client.create_run_from_pipeline_func(cal_pipeline,arguments={},experiment_name="my-experiment", run_name="test-run-1", namespace="kubeflow-user-example-com")