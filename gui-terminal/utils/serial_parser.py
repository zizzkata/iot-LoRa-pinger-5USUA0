def parse_serial_output(serialOutput: str):
    outputList = serialOutput.split(';')
    output = {}
    if len(outputList) == 4:
        output['code'] = outputList[0]
        output['option'] = outputList[1]
        output['data'] = outputList[2]
        output['sign'] = outputList[3]
    else:
        print("Invalid serial output")
        return None
    return output