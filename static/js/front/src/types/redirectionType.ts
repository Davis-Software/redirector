interface RedirectionType{
    id: number;
    url: string;
    slug: string;
    created_at: string;
    updated_at: string;
    archived: boolean;
    enabled: boolean;
    clicks: number;
    name: string;
}

export default RedirectionType;
