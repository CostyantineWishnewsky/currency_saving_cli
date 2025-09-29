
import sys
import asyncio

from router import ROUTER,handle_controller_result


async def main()->None:
    args = sys.argv[1:]

    if not args:
        # await ROUTER['help']([])
        controller_result=await ROUTER['help']([])
        return
    if args[0] in ROUTER.keys():
        if type(ROUTER[args[0]]) == dict:
            if len(args) == 1:
                if '' in ROUTER[args[0]].keys():
                    # await ROUTER[args[0]]['']([])
                    result=await ROUTER[args[0]]['']([])
                    await handle_controller_result(result=result)
                    return
                # await ROUTER['help']([args[0]])
                result=await ROUTER['help']([args[0]])
                await handle_controller_result(result=result)
                return
            if args[1] in ROUTER[args[0]].keys():
                # await ROUTER[args[0]][args[1]](args[2:])
                result=await ROUTER[args[0]][args[1]](args[2:])
                await handle_controller_result(result=result)
            return
        # await ROUTER[args[0]](args[1:])
        result=await ROUTER[args[0]](args[1:])
        await handle_controller_result(result=result)
        return
    result=await ROUTER['help']([])
    await handle_controller_result(result=result)

    

if __name__ == "__main__":
    asyncio.run(main())