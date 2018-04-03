
import numpy as np
import pandas as pd
import xarray as xr


def sample_data(nyears=10, nvars=4):
    dims = ('time', 'lat', 'lon')
    variables = ('var_%d' % i for i in range(4))
    ntimes = nyears*365
    shape = (ntimes, 360, 180)
    coords = {
        'time': pd.date_range('1970-01-01', freq='1D', periods=ntimes),
        'lon': np.linspace(0, 360, shape[1]),
        'lat': np.linspace(-90, 90, shape[2])}
    ds = xr.Dataset((v, xr.DataArray(np.random.random(shape), dims=dims,
                                     coords=coords)) for v in variables)

    return ds


def
