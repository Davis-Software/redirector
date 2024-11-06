import React from "react";
import {Fade, Paper} from "@mui/material";
import {TransitionGroup} from "react-transition-group";

interface PageBaseProps {
    children: React.ReactNode | React.ReactNode[] | React.ReactElement | React.ReactElement[];
}
function PageBase(props: PageBaseProps) {
    return (
        <TransitionGroup component={null}>
            <Fade>
                <Paper>{props.children}</Paper>
            </Fade>
        </TransitionGroup>
    )
}

export default PageBase;