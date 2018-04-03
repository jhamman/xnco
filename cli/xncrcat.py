
import click
import xarray as xr

from xnco.core import get_client, get_logger


@click.command()
@click.argument('in_files', nargs=-1)
@click.argument('output', nargs=1)
@click.option('--dask-scheduler', type=str, default=None,
              help='Filename to JSON encoded scheduler information. ')
def main(in_files, out_file, dask_scheduler, log_level):

    logger = get_logger(__file__, log_level)

    # dask setup
    client = get_client(dask_scheduler)
    logger.info(client)

    # the guts of ncrcat
    ds = xr.open_mfdataset(in_files)
    ds.to_netcdf(out_file)


if __name__ == '__main__':
    main()
