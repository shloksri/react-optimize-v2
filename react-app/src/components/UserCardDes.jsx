import PropTypes from "prop-types";
import { memo } from "react";

const UserCardDes = ({ id, name, email, role }) => {
  return (
    <tr>
      <td className="border px-2 py-4 w-0.5">{id}</td>
      <td className="border px-2 py-4">{name}</td>
      <td className="border px-2 py-4">{email}</td>
      <td className="border px-2 py-4">{role}</td>
    </tr>
  );
};

export default memo(UserCardDes);
