import esmlab


def sel_time(ds, indexer_val, time_coord_name=None, year_offset=None):
    esmlabacc = ds.esmlab.set_time(time_coord_name=time_coord_name)
    time_coord_name = esmlabacc.time_coord_name
    dso = esmlabacc.compute_time_var(year_offset=year_offset).sel(**{time_coord_name: indexer_val})
    esmlabacc = dso.esmlab.set_time(time_coord_name=time_coord_name)
    return esmlabacc.uncompute_time_var()