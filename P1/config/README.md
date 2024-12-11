# Connect ank agent with ank server
```bash
ank-agent -k --name <AGENT_NAME> --server-url http://$SERVER_IP:25551
```

# Update the state of Ankaios system (workload)
```bash
ank -k set state desiredState.workloads.<WORKLOAD_NAME> <SET_FILE_NAME>
```

#  Apply Ankaios manifest content or file(s)
```bash
ank -k apply --agent <AGENT_NAME> <APPLY_FILE_NAME>
``` 

# Delete the workload
```bash 
ank -k delete workload <WORKLOAD_NAME>
```
