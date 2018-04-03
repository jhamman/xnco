
import click
import xarray as xr


@click.command()
@click.argument('in_files', nargs=-1)
def main(in_files):

    # the guts of ncdump
    ds = xr.open_mfdataset(in_files)
    ds.info()


if __name__ == '__main__':
    main()
