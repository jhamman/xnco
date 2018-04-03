
import click
import xarray as xr

from xnco.core import get_client, get_logger


@click.command()
@click.argument('in_nc', nargs=1)
@click.argument('out_nc', nargs=1)
@click.option('--dask-scheduler', type=str, default=None,
              help='Filename to JSON encoded scheduler information.')
@click.option('--log_level', default='INFO', show_default=True,
              help='logging level, useful for debugging')
def main(in_nc, out_nc, dask_scheduler, log_level):

    logger = get_logger(__file__, log_level)

    # dask setup
    client = get_client(dask_scheduler)
    logger.info(client)

    # the guts of ncrcat
    ds = xr.open_dataset(in_nc)
    ds.to_netcdf(out_nc)


if __name__ == '__main__':
    main()
