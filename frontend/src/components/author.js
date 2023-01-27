import React from 'react'


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.first_name}
            </td>
             <td>
                {author.last_name}
            </td>
             <td>
                {author.age}
            </td>
        </tr>
    )
}


const AuthorList = ({authors}) => {
    return (
        <table>
            <thead>
                <th>
                    First Name
                </th>
                 <th>
                    Last Name
                </th>
                 <th>
                    Age
                </th>
                {authors.map((author) => <AuthorItem author={author}/>)}
            </thead>
        </table>
    )
}

export default AuthorList;