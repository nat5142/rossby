## **Rossby**
A wrapper for the National Weather Service API

#### Rossby Lite (metaclass backend)

##### Hi Chad!

Within the main `Rossby` module, I've built a "lite" API wrapper, stripped of many
of the features I'm hoping to add to the main version. I've basically used this as
a vehicle to familiarize myself with `metaprogramming`.

Everything that is used to construct this wrapper is contained in the directory you
are currently in. There are 3 files that wrap the entire API:

- `lite/rossby.py`
- `lite/api_config.py`
- `lite/resultset.py` _(I actually don't even know if this works yet)_

That's it!!

All of the endpoints can be found in the file `api_config.py`, variable `api_endpoints`.

----------------------------------

##### Try this, from the top-level directory:

```python
from lite.rossby import Rossby


rossby = Rossby()


print(rossby.stations.by_id(station_id='KUNV'))
print(rossby.alerts.get_active())
```
