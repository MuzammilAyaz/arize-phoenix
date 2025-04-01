from openinference.instrumentation.dspy import DSPyInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from openinference.instrumentation import using_metadata

endpoint = "http://localhost:6006/v1/traces"
tracer_provider = trace_sdk.TracerProvider()
trace_api.set_tracer_provider(tracer_provider)
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))

DSPyInstrumentor().instrument()

import dspy
import os
from dotenv import load_dotenv
load_dotenv()
azure_llm = dspy.LM(
    os.environ["AZURE_OPENAI_MODEL"],
    api_base=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_version=os.environ["AZURE_OPENAI_VERSION"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    temperature=0.1
)

metadata = {
    "req_id" : "1231232"
}
# with using_attributes(
#     session_id="my-session-id",
#     user_id="my-user-id",
#     metadata=metadata,
#     tags=tags,
#     prompt_template=prompt_template,
#     prompt_template_version=prompt_template_version,
#     prompt_template_variables=prompt_template_variables,
# ):
with (using_metadata(metadata)):
    print(azure_llm("meowowwwohahahhaass"))