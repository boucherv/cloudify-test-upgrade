from cloudify.decorators import workflow
from cloudify.workflows import ctx

@workflow
def run_operation(operation, nodes_type_update, operation_kwargs, **kwargs):
    graph = ctx.graph_mode()

    for node in ctx.nodes:
            for instance in node.instances:

                sequence = graph.sequence()

                sequence.add(
                    instance.send_event('Starting to run operation'),
                    instance.execute_operation(operation, kwargs=operation_kwargs),
                    instance.send_event('Done running operation'))

    return graph.execute()

