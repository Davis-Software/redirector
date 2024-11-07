import React from "react";
import HideOnScroll from "../../utils/HideOnScroll";
import {AppBar, Box, Tab, Tabs, Toolbar} from "@mui/material";
import {navigateTo} from "../../utils/navigation";


interface NavBarProps{
    page: string,
    navItems: [string, string][]
}
function NavBar(props: NavBarProps){
    return (
        <>
            <HideOnScroll>
                <AppBar>
                    <Box>
                        <Tabs
                            value={props.page}
                            onChange={(_, value) => {
                                navigateTo(value)
                            }}
                            variant="scrollable"
                        >
                            {props.navItems.map(item => (
                                <Tab
                                    key={item[0]}
                                    label={item[0]}
                                    value={item[1]}
                                />
                            ))}
                        </Tabs>
                    </Box>
                </AppBar>
            </HideOnScroll>
            <Toolbar sx={{minHeight: "48px !important"}} />
        </>
    )
}

export default NavBar