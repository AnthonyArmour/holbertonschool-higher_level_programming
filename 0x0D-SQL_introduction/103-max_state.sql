-- displays list of max temps for states
SELECT `state`, MAX(`value`) AS max_temp FROM temperatures GROUP BY `state` ORDER BY `state`;