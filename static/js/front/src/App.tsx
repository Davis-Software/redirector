import React, {lazy, Suspense, useState} from "react"
import {ThemeProvider} from "@mui/material";
import defaultTheme from "./themes/defaultTheme";
import PageLoader from "./components/PageLoader";
import NavBar from "./components/navigation/NavBar";

const Stats = lazy(() => import("./pages/Stats"))
const Redirects = lazy(() => import("./pages/Redirects"))

interface PageRendererProps{
    page: string
}
function PageRenderer(props: PageRendererProps){
    switch (props.page){
        case "stats":
            return <Stats />
        case "redirects":
            return <Redirects />
    }
}

function App(){
    const [page, setPage] = useState<string>("stats")

    return (
        <ThemeProvider theme={defaultTheme}>
            <NavBar value={page} onChange={setPage} />
            <Suspense fallback={<PageLoader />}>
                <PageRenderer page={page} />
            </Suspense>
        </ThemeProvider>
    )
}

export default App;
