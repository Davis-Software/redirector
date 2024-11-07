import React, {useEffect, useState} from "react";
import PageBase from "./PageBase";
import RedirectionType from "../types/redirectionType";
import {Button, ButtonGroup, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";


type Order = "asc" | "desc"
type SortBy = "name" | "clicks" | "updated_at" | "created_at"


interface RedirectionTableRowProps {
    redirection: RedirectionType
    onClick: (redirection: RedirectionType) => void
    onEdit: (redirection: RedirectionType) => void
    onDelete: (redirection: RedirectionType) => void
    onActivatedChange: (redirection: RedirectionType) => void
}
function RedirectionTableRow(props: RedirectionTableRowProps){
    return (
        <TableRow onClick={() => props.onClick(props.redirection)} hover>
            <TableCell padding="checkbox">{props.redirection.enabled}</TableCell>
            <TableCell>{props.redirection.name}</TableCell>
            <TableCell>{props.redirection.slug}</TableCell>
            <TableCell>{props.redirection.clicks}</TableCell>
            <TableCell>Graph</TableCell>
            <TableCell>{props.redirection.created_at}</TableCell>
            <TableCell>{props.redirection.updated_at}</TableCell>
            <TableCell align="right">
                <ButtonGroup size="small">
                    <Button
                        color="secondary"
                        onClick={() => props.onEdit(props.redirection)}
                    >Deactivate</Button>
                    <Button color="warning" onClick={() => props.onEdit(props.redirection)}>Edit</Button>
                    <Button color="error" onClick={() => props.onEdit(props.redirection)}>Delete</Button>
                </ButtonGroup>
            </TableCell>
        </TableRow>
    )
}


interface RedirectionsTableProps {
    redirections: RedirectionType[]
    setSortBy: (sortBy: SortBy) => void
    setOrder: (order: Order) => void
    onClick: (redirection: RedirectionType) => void
    onEdit: (redirection: RedirectionType) => void
    onDelete: (redirection: RedirectionType) => void
}
function RedirectionsTable(props: RedirectionsTableProps){
    return (
        <TableContainer>
            <Table stickyHeader>
                <TableHead>
                    <TableRow>
                        <TableCell padding="checkbox"></TableCell>
                        <TableCell>Name</TableCell>
                        <TableCell>URL</TableCell>
                        <TableCell>Clicks</TableCell>
                        <TableCell>Usage Graph</TableCell>
                        <TableCell>Created At</TableCell>
                        <TableCell>Updated At</TableCell>
                        <TableCell align="right">Actions</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {props.redirections.map((redirection, index) => (
                        <RedirectionTableRow
                            key={index}
                            redirection={redirection}
                            onClick={props.onClick}
                            onEdit={props.onEdit}
                            onDelete={props.onDelete}
                        />
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    )
}


function Redirections(){
    const [redirections, setRedirections] = useState<RedirectionType[]>([])

    const [page, setPage] = useState<number>(1)
    const [search, setSearch] = useState<string>("")
    const [sortBy, setSortBy] = useState<SortBy>("created_at")
    const [order, setOrder] = useState<Order>("desc")

    useEffect(() => {
        fetch(`/api/redirections?page=${page}&search=${search}&sort_by=${sortBy}&order=${order}`)
            .then(response => response.json())
            .then(data => {
                if(page === 1){
                    setRedirections(data)
                }else{
                    setRedirections([...redirections, ...data])
                }
            })
    }, [page, sortBy, order]);
    useEffect(() => {
        setPage(1)
    }, [search]);

    return (
        <PageBase>
            <RedirectionsTable redirections={redirections} setSortBy={setSortBy} setOrder={setOrder} />
        </PageBase>
    )
}

export default Redirections;
