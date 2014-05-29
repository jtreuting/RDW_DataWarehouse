__author__ = 'sravi'

import os
import logging
from edcore.watch.util import SendFileUtil
from edcore.watch.util import FileUtil
from edcore.watch.constants import MoverConstants as MoverConst, WatcherConstants as WatcherConst
from edcore.exceptions import RemoteCopyError
from edcore import DEFAULT_LOGGER_NAME


class FileMover():
    """File mover class to move files to needed destination"""

    def __init__(self, config, append_logs_to=DEFAULT_LOGGER_NAME):
        self.conf = config
        self.logger = logging.getLogger(append_logs_to)

    def move_files(self, files_to_move):
        files_moved = 0
        # sort by file length in to get all checksum files sent first before source files
        files_to_move.sort(key=len)
        for file in files_to_move:
            self.logger.debug('SFTPing file: ' + file)
            file_tenant_name, file_tenant_user_name = \
                FileUtil.get_file_tenant_and_user_name(file, os.path.join(self.conf.get(WatcherConst.BASE_DIR),
                                                                          self.conf.get(WatcherConst.SOURCE_DIR)))
            try:
                file_transfer_status = \
                    SendFileUtil.remote_transfer_file(
                        source_file=file, hostname=self.conf.get(MoverConst.LANDING_ZONE_HOSTNAME),
                        remote_base_dir=self.conf.get(MoverConst.ARRIVALS_PATH), file_tenantname=file_tenant_name,
                        file_username=file_tenant_user_name, sftp_username=self.conf.get(MoverConst.SFTP_USER),
                        private_key_file=self.conf.get(MoverConst.PRIVATE_KEY_FILE))
                if file_transfer_status == 0:
                    self.logger.debug('File transfer was success for {file}'.format(file=file))
                    os.remove(file)
                    files_moved += 1
                    self.logger.debug('Deleted source file {file}'.format(file=file))
            except RemoteCopyError as e:
                self.logger.error('File transfer failed for {file} '
                                  'with error {error}'.format(file=file, error=str(e)))
        return files_moved