import React from "react";
import PageBase from "../pages/PageBase";
import {CircularProgress} from "@mui/material";

function SwcCenteredLoader(props: {className?: string}) {
    return (
        <div className={"d-flex justify-content-center " + props.className}>
            <CircularProgress />
        </div>
    )
}

function PageLoader(){
    return (
        <PageBase>
            <SwcCenteredLoader className="swc-loader-middle" />
        </PageBase>
    )
}

export default PageLoader;
export {SwcCenteredLoader};