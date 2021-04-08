"""OpenAPI core contrib falcon responses module"""
from openapi_core.validation.response.datatypes import OpenAPIResponse


class FalconOpenAPIResponseFactory(object):
    @classmethod
    def create(cls, response):
        status_code = int(response.status[:3])

        mimetype = ''
        if response.content_type:
            mimetype = response.content_type.partition(";")[0]
        else:
            mimetype = response.options.default_media_type

        return OpenAPIResponse(
            data=response.text,
            status_code=status_code,
            mimetype=mimetype,
        )
