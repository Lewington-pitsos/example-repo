from code import interact
from multiprocessing.sharedctypes import Value

from numpy import record


class SalesforceRecords():
    def __init__(self, recordIds) -> None:
        self.recordIds = recordIds
    


class ODWClient():
    def __init__(self, odw_params) -> None:
        # initialize a client to oracle data warehouse with those parameteres 
        pass

    def save_records(records):
        pass

    def delete_records(record_ids):
        pass

class Record():
    def __init__(self) -> None:
        pass


def looks_normal(record):
    return True

# Saving records

def perform_migration(record_ids):
    odw_client = ODWClient("something")
    record_itr = SalesforceRecords(record_ids)

    saved_record_ids = []
    for rec in record_itr:
        if not looks_normal(record):
            odw_client.delete_records(saved_record_ids)
            raise ValueError("record did not look normal, reverted all saved records", rec)
        else:
            odw_client.save(rec)
            saved_record_ids.append(rec.id)
    
    odw_client.close()

def matches_exactly(a, b):
    return True

# Confirming that records have been saved correctly

def perform_test(record_ids):
    record_itr = SalesforceRecords(record_ids)
    odw_client = ODWClient("something")
    
    for rec in record_itr:
        saved_rec = odw_client.get_record(rec.id)
        if not matches_exactly(rec, saved_rec):
            raise ValueError("saved record", rec, "did not match original record", rec, "exactly")