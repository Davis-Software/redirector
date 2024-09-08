import React from "react"
import {TableCell, TableRow, TableHead, Table} from "@mui/material";

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
        <Table>
            <TableHeader />
        </Table>
    )
}

export default Redirects