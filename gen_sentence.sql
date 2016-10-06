select dt, collect_list(code)
from (
	select dt, code, price_diff
	from stock_diff_data
	where length(code) == 6
	order by dt, price_diff
) as A
group by dt
order by dt
;
