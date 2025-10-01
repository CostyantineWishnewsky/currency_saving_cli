

from support.ControllerResult import ControllerResult,ControllerResultStatus,OkData,ErrorData,RedirectData



def result_ok_empty()->ControllerResult:
    return ControllerResult(status=ControllerResultStatus.Ok.value,data=None)

def result_redirect(route_to:str,arguments:list[str])->ControllerResult:
    data=RedirectData(route_to=route_to,arguments=arguments)
    return ControllerResult(status=ControllerResultStatus.Redirect.value,data=data)

def result_error(error_message:str)->ControllerResult:
    return ControllerResult(status=ControllerResultStatus.Error,error_message=error_message)