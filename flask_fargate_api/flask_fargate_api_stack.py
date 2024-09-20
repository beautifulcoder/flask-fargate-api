from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_logs as logs
)
from constructs import Construct


class FlaskFargateApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "vpc"
        )

        cluster = ecs.Cluster(
            self,
            "cluster",
            vpc=vpc
        )

        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "api",
            cluster=cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=1,
            public_load_balancer=True,

            task_image_options={
                "environment": {
                    "ADDRESS": "0.0.0.0",
                    "PORT": "80"
                },
                "image": ecs.ContainerImage.from_asset(
                    directory="app"
                ),
                "container_port": 80,
                "log_driver": ecs.AwsLogDriver(
                    stream_prefix="api",
                    log_retention=logs.RetentionDays.ONE_DAY
                )
            }
        )

        service.target_group.configure_health_check(
            path="/health"
        )
