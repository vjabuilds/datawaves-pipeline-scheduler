from airflow.models.baseoperator import BaseOperator

class PipelineOperator(BaseOperator):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
    
    def execute(self, context):
        print('Hello, I am', self.name)
        return self.name