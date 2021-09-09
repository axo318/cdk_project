#!/usr/bin/env python3
import os

from aws_cdk import core

from cdk_project.cdk_project_stack import CdkProjectStack
from cdk_project.pipeline_stack import PipelineStack


app = core.App()
CdkProjectStack(app, "CdkProjectStack")
PipelineStack(app, "CdkProjectPipelineStack", env={
    'account': '090841905266',
    'region': 'eu-central-1'
})

app.synth()
