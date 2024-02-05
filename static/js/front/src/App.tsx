import React from "react"
import {ThemeProvider} from "@mui/material";
import defaultTheme from "./themes/defaultTheme";

function App(){
    return (
        <ThemeProvider theme={defaultTheme}>



        </ThemeProvider>
    )
}

export default App;
