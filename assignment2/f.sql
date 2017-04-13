select count(distinct docid) from Frequency where term = 'transactions'
and docid in (select distinct docid from Frequency where term = 'world');
