import sys
filepath = sys.argv[1]
print("It worked",sys.argv[1])

from plottr.data.datadict_storage import all_datadicts_from_hdf5
from plottr.apps.autoplot import main

main(filepath,'data')