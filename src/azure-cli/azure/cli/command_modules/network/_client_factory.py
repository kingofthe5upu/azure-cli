# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def network_client_factory(cli_ctx, **kwargs):
    from azure.cli.core.profiles import ResourceType
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_NETWORK, **kwargs)


def resource_client_factory(cli_ctx, **_):
    from azure.cli.core.profiles import ResourceType
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_RESOURCE_RESOURCES)


def cf_connection_monitor(cli_ctx, _):
    return network_client_factory(cli_ctx).connection_monitors


def cf_flow_logs(cli_ctx, _):
    return network_client_factory(cli_ctx).flow_logs


def cf_private_link_services(cli_ctx, _):
    return network_client_factory(cli_ctx).private_link_services


def cf_load_balancers(cli_ctx, _):
    return network_client_factory(cli_ctx).load_balancers


def cf_load_balancer_backend_pools(cli_ctx, _):
    return network_client_factory(cli_ctx).load_balancer_backend_address_pools


def cf_local_network_gateways(cli_ctx, _):
    return network_client_factory(cli_ctx).local_network_gateways


def cf_network_interfaces(cli_ctx, _):
    return network_client_factory(cli_ctx).network_interfaces


def cf_network_watcher(cli_ctx, _):
    return network_client_factory(cli_ctx).network_watchers


def cf_packet_capture(cli_ctx, _):
    return network_client_factory(cli_ctx).packet_captures


def cf_private_access(cli_ctx, _):
    return network_client_factory(cli_ctx).available_private_access_services


def cf_virtual_network_gateway_connections(cli_ctx, _):
    return network_client_factory(cli_ctx).virtual_network_gateway_connections


def cf_virtual_network_gateways(cli_ctx, _):
    return network_client_factory(cli_ctx).virtual_network_gateways


def cf_dns_references(cli_ctx, _):
    from azure.cli.core.profiles import ResourceType
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_NETWORK_DNS).dns_resource_reference


def cf_dns_mgmt_zones(cli_ctx, _):
    from azure.cli.core.profiles import ResourceType
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_NETWORK_DNS).zones


def cf_dns_mgmt_record_sets(cli_ctx, _):
    from azure.cli.core.profiles import ResourceType
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_NETWORK_DNS).record_sets


def cf_virtual_router(cli_ctx, _):
    return network_client_factory(cli_ctx).virtual_routers


def cf_virtual_hub(cli_ctx, _):
    return network_client_factory(cli_ctx).virtual_hubs


def cf_virtual_router_peering(cli_ctx, _):
    return network_client_factory(cli_ctx).virtual_router_peerings
