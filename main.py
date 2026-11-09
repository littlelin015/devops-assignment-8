from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)

# Initialize tracer provider
provider = TracerProvider()
provider.add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("assignment8.demo")

# Create parent and child spans
with tracer.start_as_current_span("checkout"):
    print("Starting checkout...")

    with tracer.start_as_current_span("charge-card"):
        print("Payment successful!")

    print("Checkout completed!")
