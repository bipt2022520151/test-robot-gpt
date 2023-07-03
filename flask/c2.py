import nacos
from fastapi import FastAPI

from c1 import fastapi_router


def register_server_to_nacos():
    nacos_server_addresses = '192.168.8.246:8848'
    nacos_namespace = 'public'
    nacos_user = 'xxxxxx'
    nacos_password = '123456'
    nacos_cluster_name = 'DEFAULT'
    nacos_group_name = 'DEFAULT_GROUP'
    nacos_project_service_name = 'data-quality-system'
    nacos_project_service_ip = '192.168.8.111'
    nacos_project_service_port = 6060

    client = nacos.NacosClient(nacos_server_addresses,
                               namespace=nacos_namespace,
                               username=nacos_user,
                               password=nacos_password)

    client.add_naming_instance(nacos_project_service_name,
                               nacos_project_service_ip,
                               nacos_project_service_port,
                               cluster_name=nacos_cluster_name,
                               weight=1,
                               metadata=None,
                               enable=True,
                               healthy=True,
                               ephemeral=False,
                               group_name=nacos_group_name)

    client.send_heartbeat(nacos_project_service_name,
                          nacos_project_service_ip,
                          nacos_project_service_port,
                          cluster_name=nacos_cluster_name,
                          weight=1,
                          metadata=None,
                          ephemeral=False,
                          group_name=nacos_group_name)


app = FastAPI(title='my_fastapi_docs', description='my_fastapi_docs')
app.include_router(router=fastapi_router.fastapi_router)

if __name__ == '__main__':
    register_server_to_nacos()

import uvicorn

uvicorn.run(app=app, host="0.0.0.0", port=8080, workers=1)
