import React from "react"
import {TableCell, TableRow, TableHead, Table, Box} from "@mui/material";
import {SwcFab, SwcFabContainer} from "../components/SwcFab";

function TableHeader(){
    return (
        <TableHead>
            <TableRow>
                <TableCell>Name</TableCell>
                <TableCell>Code</TableCell>
                <TableCell>Target</TableCell>
            </TableRow>
        </TableHead>
    )
}

function Redirects(){
    return (
        <Box>
            <Table>
                <TableHeader />
            </Table>
            <SwcFabContainer>
                <SwcFab icon="add" onClick={() => {}} color="primary" tooltip="Add Redirect" tooltipPlacement="left" />
            </SwcFabContainer>
        </Box>
    )
}

export default Redirects