import React, {lazy, Suspense, useEffect, useMemo, useState} from "react"

import defaultTheme from "./themes/defaultTheme";

const NavBar = lazy(() => import("./components/navigation/NavBar"));

import {CssBaseline, ThemeProvider} from "@mui/material";
import {setWindowTitle} from "./utils/navigation";
import PageLoader from "./components/PageLoader";

const Redirections = lazy(() => import("./pages/Redirections"));
const Settings = lazy(() => import("./pages/Settings"));

const NotFound = lazy(() => import("./pages/other/NotFound"));

const navItems: [string, string][] = [
    ["Redirections", "/"],
    ["Statistics", "/statistics"],
    ["Settings", "/settings"],
]

function App(){
    const [page, setPage] = useState(window.location.pathname || "/")

    useEffect(() => {
        function pageSetter(){
            setPage(window.location.pathname)
        }
        window.addEventListener("popstate", pageSetter)

        return () => {
            window.removeEventListener("popstate", pageSetter)
        }
    }, [])
    useEffect(() => {
        setWindowTitle(navItems.filter(item => item[1] === page)[0][0] || "Not Found")

        if(window.location.pathname === page) return
        history.pushState(null, "", page)
    }, [page])

    const RenderPage = useMemo(() => {
        switch(page){
            case "/":
                return <Redirections />
            case "/statistics":
                return null
                // return <Statistics />
            case "/settings":
                return <Settings />
            default:
                return <NotFound />
        }
    }, [page])

    return (
        <ThemeProvider theme={defaultTheme}>
            <CssBaseline />
            <NavBar page={page} navItems={navItems} />

            <Suspense fallback={<PageLoader />}>
                {RenderPage}
            </Suspense>
        </ThemeProvider>
    )
}

export default App;
