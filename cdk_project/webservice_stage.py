from aws_cdk import core

from .cdk_project_stack import CdkProjectStack

class WebServiceStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = CdkProjectStack(self, 'WebService')

        self.url_output = service.url_output
