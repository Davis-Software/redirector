import React from "react";
import HideOnScroll from "../../utils/HideOnScroll";
import {AppBar, Box, Tab, Tabs, Toolbar} from "@mui/material";


interface NavBarProps{
    value: string,
    onChange: (num: string) => void
}
function NavBar(props: NavBarProps){
    return (
        <>
            <HideOnScroll>
                <AppBar>
                    <Box>
                        <Tabs
                            value={props.value}
                            onChange={(e: React.SyntheticEvent, v: string) => {
                                props.onChange(v)
                            }}
                            variant="scrollable"
                        >
                            <Tab value="stats" label="Statistics" />
                            <Tab value="redirects" label="Redirects" />
                            <Tab value="settings" label="Settings" />
                        </Tabs>
                    </Box>
                </AppBar>
            </HideOnScroll>
            <Toolbar sx={{minHeight: "48px !important"}} />
        </>
    )
}

export default NavBar